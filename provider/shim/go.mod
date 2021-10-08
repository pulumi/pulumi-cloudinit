module github.com/hashicorp/terraform-provider-cloudinit/shim

go 1.15

require (
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.4.3
	github.com/hashicorp/terraform-provider-cloudinit v1.0.1-0.20210219131110-b7f8b5106bd2
)

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20201218231525-9cca98608a5e
