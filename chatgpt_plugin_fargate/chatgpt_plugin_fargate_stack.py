from aws_cdk import (
    Stack,
    aws_ecs_patterns,
    aws_secretsmanager as sm,
    aws_ecs as ecs,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_logs
)
from aws_cdk.aws_ecs import ContainerImage
from constructs import Construct


class MyFargateService(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(
            scope,
            id,
            **kwargs
        )

        secret = sm.Secret.from_secret_name_v2(self, "chatgpt_plugin_secret", "chatgpt_plugin_secret")

        self.service = aws_ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "MyFargateService",
            cpu=256,
            memory_limit_mib=512,
            desired_count=1,
            public_load_balancer=True,
            task_image_options={
                "image": ContainerImage.from_asset("src"),
                "secrets": {
                    "OPENAI_API_KEY": ecs.Secret.from_secrets_manager(secret, "OPENAI_API_KEY"),
                    "GOOGLE_CSE_ID": ecs.Secret.from_secrets_manager(secret, "GOOGLE_CSE_ID"),
                    "GOOGLE_API_KEY": ecs.Secret.from_secrets_manager(secret, "GOOGLE_API_KEY"),
                },
                "log_driver": ecs.AwsLogDriver(
                    stream_prefix="ChatBotPlugin",
                    log_group=aws_logs.LogGroup(
                        self, "ServiceLogs",
                        log_group_name="FargateService",
                        retention=aws_logs.RetentionDays.ONE_WEEK)
                ),
            },
        )

        hosted_zone = route53.HostedZone(
            self,
            "HostedZone",
            zone_name="giftsuggesterplugin.life",
        )

        route53.ARecord(
            self,
            "AliasRecord",
            zone=hosted_zone,
            record_name="www",  # replace with your preferred subdomain
            target=route53.RecordTarget.from_alias(
                targets.LoadBalancerTarget(self.service.load_balancer)
            ),
        )


class ChatgptPluginFargateStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fargate = MyFargateService(self, "fargateService")
