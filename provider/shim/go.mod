module github.com/hashicorp/terraform-provider-cloudinit/shim

go 1.22.7

require (
	github.com/hashicorp/terraform-plugin-framework v1.11.0
	github.com/hashicorp/terraform-provider-cloudinit v1.0.1-0.20240910114655-9216daa4c24b
)

require (
	github.com/fatih/color v1.16.0 // indirect
	github.com/hashicorp/go-hclog v1.6.3 // indirect
	github.com/hashicorp/terraform-plugin-framework-validators v0.13.0 // indirect
	github.com/hashicorp/terraform-plugin-go v0.23.0 // indirect
	github.com/hashicorp/terraform-plugin-log v0.9.0 // indirect
	github.com/mattn/go-colorable v0.1.13 // indirect
	github.com/mattn/go-isatty v0.0.20 // indirect
	github.com/mitchellh/go-testing-interface v1.14.1 // indirect
	github.com/vmihailenco/msgpack/v5 v5.4.1 // indirect
	github.com/vmihailenco/tagparser/v2 v2.0.0 // indirect
	golang.org/x/sys v0.23.0 // indirect
)

replace (
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220824175045-450992f2f5b9
	google.golang.org/genproto => google.golang.org/genproto v0.0.0-20231002182017-d307bd883b97
)
