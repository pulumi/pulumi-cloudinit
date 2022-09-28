// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudinit

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
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
//
//	"github.com/pulumi/pulumi-cloudinit/sdk/go/cloudinit"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := cloudinit.LookupConfig(ctx, &GetConfigArgs{
//				Base64Encode: pulumi.BoolRef(false),
//				Gzip:         pulumi.BoolRef(false),
//				Parts: []GetConfigPart{
//					GetConfigPart{
//						Content:     "baz",
//						ContentType: pulumi.StringRef("text/x-shellscript"),
//						Filename:    pulumi.StringRef("foobar.sh"),
//					},
//				},
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupConfig(ctx *pulumi.Context, args *LookupConfigArgs, opts ...pulumi.InvokeOption) (*LookupConfigResult, error) {
	var rv LookupConfigResult
	err := ctx.Invoke("cloudinit:index/getConfig:getConfig", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getConfig.
type LookupConfigArgs struct {
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
	Parts []GetConfigPart `pulumi:"parts"`
}

// A collection of values returned by getConfig.
type LookupConfigResult struct {
	Base64Encode *bool   `pulumi:"base64Encode"`
	Boundary     *string `pulumi:"boundary"`
	Gzip         *bool   `pulumi:"gzip"`
	// The provider-assigned unique ID for this managed resource.
	Id    string          `pulumi:"id"`
	Parts []GetConfigPart `pulumi:"parts"`
	// The final rendered multi-part cloud-init config.
	Rendered string `pulumi:"rendered"`
}

func LookupConfigOutput(ctx *pulumi.Context, args LookupConfigOutputArgs, opts ...pulumi.InvokeOption) LookupConfigResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupConfigResult, error) {
			args := v.(LookupConfigArgs)
			r, err := LookupConfig(ctx, &args, opts...)
			var s LookupConfigResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupConfigResultOutput)
}

// A collection of arguments for invoking getConfig.
type LookupConfigOutputArgs struct {
	// Base64 encoding of the rendered output. Defaults to `true`,
	// and cannot be disabled if `gzip` is `true`.
	Base64Encode pulumi.BoolPtrInput `pulumi:"base64Encode"`
	// Define the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
	Boundary pulumi.StringPtrInput `pulumi:"boundary"`
	// Specify whether or not to gzip the rendered output. Defaults to `true`.
	Gzip pulumi.BoolPtrInput `pulumi:"gzip"`
	// A nested block type which adds a file to the generated
	// cloud-init configuration. Use multiple `part` blocks to specify multiple
	// files, which will be included in order of declaration in the final MIME
	// document.
	Parts GetConfigPartArrayInput `pulumi:"parts"`
}

func (LookupConfigOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConfigArgs)(nil)).Elem()
}

// A collection of values returned by getConfig.
type LookupConfigResultOutput struct{ *pulumi.OutputState }

func (LookupConfigResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConfigResult)(nil)).Elem()
}

func (o LookupConfigResultOutput) ToLookupConfigResultOutput() LookupConfigResultOutput {
	return o
}

func (o LookupConfigResultOutput) ToLookupConfigResultOutputWithContext(ctx context.Context) LookupConfigResultOutput {
	return o
}

func (o LookupConfigResultOutput) Base64Encode() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupConfigResult) *bool { return v.Base64Encode }).(pulumi.BoolPtrOutput)
}

func (o LookupConfigResultOutput) Boundary() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupConfigResult) *string { return v.Boundary }).(pulumi.StringPtrOutput)
}

func (o LookupConfigResultOutput) Gzip() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupConfigResult) *bool { return v.Gzip }).(pulumi.BoolPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupConfigResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConfigResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupConfigResultOutput) Parts() GetConfigPartArrayOutput {
	return o.ApplyT(func(v LookupConfigResult) []GetConfigPart { return v.Parts }).(GetConfigPartArrayOutput)
}

// The final rendered multi-part cloud-init config.
func (o LookupConfigResultOutput) Rendered() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConfigResult) string { return v.Rendered }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupConfigResultOutput{})
}
