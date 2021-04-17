// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.
// +build nodejs all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
	"github.com/stretchr/testify/assert"
)

func TestCloudInitTs(t *testing.T) {
	test := getJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(getCwd(t), "ts"),
			ExtraRuntimeValidation: func(t *testing.T, info integration.RuntimeValidationStackInfo) {
				expected := "Content-Type: multipart/mixed; boundary=\"MIMEBOUNDARY\"\nMIME-Version: 1.0" +
					"\r\n\r\n--MIMEBOUNDARY\r\nContent-Disposition: attachment; filename=\"foobar.sh\"\r\n" +
					"Content-Transfer-Encoding: 7bit\r\nContent-Type: text/x-shellscript\r\nMime-Version: 1.0" +
					"\r\n\r\nbaz\r\n--MIMEBOUNDARY--\r\n"
				assert.Equal(t, expected, info.Outputs["dsConfig"])
				assert.Equal(t, expected, info.Outputs["resourceConfig"])
			},
		})

	integration.ProgramTest(t, &test)
}

func getJSBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions()
	baseJS := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"@pulumi/cloudinit",
		},
	})

	return baseJS
}
