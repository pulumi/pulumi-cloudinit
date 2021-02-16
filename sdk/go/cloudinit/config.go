// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudinit

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type Config struct {
	pulumi.CustomResourceState

	Base64Encode pulumi.BoolPtrOutput   `pulumi:"base64Encode"`
	Boundary     pulumi.StringPtrOutput `pulumi:"boundary"`
	Gzip         pulumi.BoolPtrOutput   `pulumi:"gzip"`
	Parts        ConfigPartArrayOutput  `pulumi:"parts"`
	// rendered cloudinit configuration
	Rendered pulumi.StringOutput `pulumi:"rendered"`
}

// NewConfig registers a new resource with the given unique name, arguments, and options.
func NewConfig(ctx *pulumi.Context,
	name string, args *ConfigArgs, opts ...pulumi.ResourceOption) (*Config, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Parts == nil {
		return nil, errors.New("invalid value for required argument 'Parts'")
	}
	var resource Config
	err := ctx.RegisterResource("cloudinit:index/config:Config", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfig gets an existing Config resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigState, opts ...pulumi.ResourceOption) (*Config, error) {
	var resource Config
	err := ctx.ReadResource("cloudinit:index/config:Config", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Config resources.
type configState struct {
	Base64Encode *bool        `pulumi:"base64Encode"`
	Boundary     *string      `pulumi:"boundary"`
	Gzip         *bool        `pulumi:"gzip"`
	Parts        []ConfigPart `pulumi:"parts"`
	// rendered cloudinit configuration
	Rendered *string `pulumi:"rendered"`
}

type ConfigState struct {
	Base64Encode pulumi.BoolPtrInput
	Boundary     pulumi.StringPtrInput
	Gzip         pulumi.BoolPtrInput
	Parts        ConfigPartArrayInput
	// rendered cloudinit configuration
	Rendered pulumi.StringPtrInput
}

func (ConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*configState)(nil)).Elem()
}

type configArgs struct {
	Base64Encode *bool        `pulumi:"base64Encode"`
	Boundary     *string      `pulumi:"boundary"`
	Gzip         *bool        `pulumi:"gzip"`
	Parts        []ConfigPart `pulumi:"parts"`
}

// The set of arguments for constructing a Config resource.
type ConfigArgs struct {
	Base64Encode pulumi.BoolPtrInput
	Boundary     pulumi.StringPtrInput
	Gzip         pulumi.BoolPtrInput
	Parts        ConfigPartArrayInput
}

func (ConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configArgs)(nil)).Elem()
}

type ConfigInput interface {
	pulumi.Input

	ToConfigOutput() ConfigOutput
	ToConfigOutputWithContext(ctx context.Context) ConfigOutput
}

func (*Config) ElementType() reflect.Type {
	return reflect.TypeOf((*Config)(nil))
}

func (i *Config) ToConfigOutput() ConfigOutput {
	return i.ToConfigOutputWithContext(context.Background())
}

func (i *Config) ToConfigOutputWithContext(ctx context.Context) ConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigOutput)
}

func (i *Config) ToConfigPtrOutput() ConfigPtrOutput {
	return i.ToConfigPtrOutputWithContext(context.Background())
}

func (i *Config) ToConfigPtrOutputWithContext(ctx context.Context) ConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigPtrOutput)
}

type ConfigPtrInput interface {
	pulumi.Input

	ToConfigPtrOutput() ConfigPtrOutput
	ToConfigPtrOutputWithContext(ctx context.Context) ConfigPtrOutput
}

type configPtrType ConfigArgs

func (*configPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Config)(nil))
}

func (i *configPtrType) ToConfigPtrOutput() ConfigPtrOutput {
	return i.ToConfigPtrOutputWithContext(context.Background())
}

func (i *configPtrType) ToConfigPtrOutputWithContext(ctx context.Context) ConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigPtrOutput)
}

// ConfigArrayInput is an input type that accepts ConfigArray and ConfigArrayOutput values.
// You can construct a concrete instance of `ConfigArrayInput` via:
//
//          ConfigArray{ ConfigArgs{...} }
type ConfigArrayInput interface {
	pulumi.Input

	ToConfigArrayOutput() ConfigArrayOutput
	ToConfigArrayOutputWithContext(context.Context) ConfigArrayOutput
}

type ConfigArray []ConfigInput

func (ConfigArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Config)(nil))
}

func (i ConfigArray) ToConfigArrayOutput() ConfigArrayOutput {
	return i.ToConfigArrayOutputWithContext(context.Background())
}

func (i ConfigArray) ToConfigArrayOutputWithContext(ctx context.Context) ConfigArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigArrayOutput)
}

// ConfigMapInput is an input type that accepts ConfigMap and ConfigMapOutput values.
// You can construct a concrete instance of `ConfigMapInput` via:
//
//          ConfigMap{ "key": ConfigArgs{...} }
type ConfigMapInput interface {
	pulumi.Input

	ToConfigMapOutput() ConfigMapOutput
	ToConfigMapOutputWithContext(context.Context) ConfigMapOutput
}

type ConfigMap map[string]ConfigInput

func (ConfigMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Config)(nil))
}

func (i ConfigMap) ToConfigMapOutput() ConfigMapOutput {
	return i.ToConfigMapOutputWithContext(context.Background())
}

func (i ConfigMap) ToConfigMapOutputWithContext(ctx context.Context) ConfigMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigMapOutput)
}

type ConfigOutput struct {
	*pulumi.OutputState
}

func (ConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Config)(nil))
}

func (o ConfigOutput) ToConfigOutput() ConfigOutput {
	return o
}

func (o ConfigOutput) ToConfigOutputWithContext(ctx context.Context) ConfigOutput {
	return o
}

func (o ConfigOutput) ToConfigPtrOutput() ConfigPtrOutput {
	return o.ToConfigPtrOutputWithContext(context.Background())
}

func (o ConfigOutput) ToConfigPtrOutputWithContext(ctx context.Context) ConfigPtrOutput {
	return o.ApplyT(func(v Config) *Config {
		return &v
	}).(ConfigPtrOutput)
}

type ConfigPtrOutput struct {
	*pulumi.OutputState
}

func (ConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Config)(nil))
}

func (o ConfigPtrOutput) ToConfigPtrOutput() ConfigPtrOutput {
	return o
}

func (o ConfigPtrOutput) ToConfigPtrOutputWithContext(ctx context.Context) ConfigPtrOutput {
	return o
}

type ConfigArrayOutput struct{ *pulumi.OutputState }

func (ConfigArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Config)(nil))
}

func (o ConfigArrayOutput) ToConfigArrayOutput() ConfigArrayOutput {
	return o
}

func (o ConfigArrayOutput) ToConfigArrayOutputWithContext(ctx context.Context) ConfigArrayOutput {
	return o
}

func (o ConfigArrayOutput) Index(i pulumi.IntInput) ConfigOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Config {
		return vs[0].([]Config)[vs[1].(int)]
	}).(ConfigOutput)
}

type ConfigMapOutput struct{ *pulumi.OutputState }

func (ConfigMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Config)(nil))
}

func (o ConfigMapOutput) ToConfigMapOutput() ConfigMapOutput {
	return o
}

func (o ConfigMapOutput) ToConfigMapOutputWithContext(ctx context.Context) ConfigMapOutput {
	return o
}

func (o ConfigMapOutput) MapIndex(k pulumi.StringInput) ConfigOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Config {
		return vs[0].(map[string]Config)[vs[1].(string)]
	}).(ConfigOutput)
}

func init() {
	pulumi.RegisterOutputType(ConfigOutput{})
	pulumi.RegisterOutputType(ConfigPtrOutput{})
	pulumi.RegisterOutputType(ConfigArrayOutput{})
	pulumi.RegisterOutputType(ConfigMapOutput{})
}
