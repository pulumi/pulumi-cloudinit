package shim

import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-provider-cloudinit/internal/provider"
)

func NewProvider() *schema.Provider {
	return provider.New()
}
