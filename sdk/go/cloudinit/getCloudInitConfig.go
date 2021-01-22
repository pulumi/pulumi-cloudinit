// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudinit

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Renders a [multipart MIME configuration](https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive)
// for use with [cloud-init](https://cloudinit.readthedocs.io/).
//
// Cloud-init is a commonly-used startup configuration utility for cloud compute
// instances. It accepts configuration via provider-specific user data mechanisms,
// such as `userData` for Amazon EC2 instances. Multipart MIME is one of the
// data formats it accepts. For more information, see
// [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/topics/format.html)
// in the cloud-init manual.
//
// This is not a generalized utility for producing multipart MIME messages. Its
// featureset is specialized for the features of cloud-init.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-cloudinit/sdk/go/cloudinit"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := false
// 		opt1 := false
// 		_, err := cloudinit.GetCloudInitConfig(ctx, &cloudinit.GetCloudInitConfigArgs{
// 			Base64Encode: &opt0,
// 			Gzip:         &opt1,
// 			Parts: []cloudinit.GetCloudInitConfigPart{
// 				cloudinit.GetCloudInitConfigPart{
// 					Content:     "baz",
// 					ContentType: "text/x-shellscript",
// 					Filename:    "foobar.sh",
// 				},
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetCloudInitConfig(ctx *pulumi.Context, args *GetCloudInitConfigArgs, opts ...pulumi.InvokeOption) (*GetCloudInitConfigResult, error) {
	var rv GetCloudInitConfigResult
	err := ctx.Invoke("cloudinit:index/getCloudInitConfig:getCloudInitConfig", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCloudInitConfig.
type GetCloudInitConfigArgs struct {
	// Base64 encoding of the rendered output. Defaults to `true`,
	// and cannot be disabled if `gzip` is `true`.
	Base64Encode *bool `pulumi:"base64Encode"`
	// Define the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
	Boundary *string `pulumi:"boundary"`
	// Specify whether or not to gzip the rendered output. Defaults to `true`.
	Gzip *bool `pulumi:"gzip"`
	// A nested block type which adds a file to the generated
	// cloud-init configuration. Use multiple `part` blocks to specify multiple
	// files, which will be included in order of declaration in the final MIME
	// document.
	Parts []GetCloudInitConfigPart `pulumi:"parts"`
}

// A collection of values returned by getCloudInitConfig.
type GetCloudInitConfigResult struct {
	Base64Encode *bool   `pulumi:"base64Encode"`
	Boundary     *string `pulumi:"boundary"`
	Gzip         *bool   `pulumi:"gzip"`
	// The provider-assigned unique ID for this managed resource.
	Id    string                   `pulumi:"id"`
	Parts []GetCloudInitConfigPart `pulumi:"parts"`
	// The final rendered multi-part cloud-init config.
	Rendered string `pulumi:"rendered"`
}
