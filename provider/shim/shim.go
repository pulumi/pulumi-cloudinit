package shim

import (
	"github.com/hashicorp/terraform-plugin-framework/provider"
	cloudinitProvider "github.com/hashicorp/terraform-provider-cloudinit/internal/provider"
)

func NewProvider() provider.Provider {
	p := cloudinitProvider.New()
	return p
}
