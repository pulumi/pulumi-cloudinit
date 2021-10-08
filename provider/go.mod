module github.com/pulumi/pulumi-cloudinit/provider

go 1.16

replace (
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20201218231525-9cca98608a5e
	github.com/hashicorp/terraform-provider-cloudinit/shim => ./shim
)

require (
	github.com/hashicorp/terraform-provider-cloudinit/shim v0.0.0
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.9.0
	github.com/pulumi/pulumi/pkg/v3 v3.14.1-0.20211007222624-789e39219452
	github.com/pulumi/pulumi/sdk/v3 v3.14.1-0.20211007222624-789e39219452
)
