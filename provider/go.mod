module github.com/pulumi/pulumi-cloudinit/provider

go 1.16

replace (
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20201218231525-9cca98608a5e
	github.com/hashicorp/terraform-provider-cloudinit/shim => ./shim
)

require (
	github.com/hashicorp/terraform-provider-cloudinit/shim v0.0.0
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.18.0
	github.com/pulumi/pulumi/sdk/v3 v3.23.2
)
