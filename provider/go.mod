module github.com/pulumi/pulumi-cloudinit/provider

go 1.15

replace (
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20201218231525-9cca98608a5e
	github.com/hashicorp/terraform-provider-cloudinit/shim => ./shim
)

require (
	github.com/hashicorp/terraform-plugin-sdk v1.9.1
	github.com/hashicorp/terraform-provider-cloudinit/shim v0.0.0
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.18.1
	github.com/pulumi/pulumi/sdk/v2 v2.18.0
)
