// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudinit;

import com.pulumi.cloudinit.Utilities;
import com.pulumi.cloudinit.inputs.GetConfigArgs;
import com.pulumi.cloudinit.inputs.GetConfigPlainArgs;
import com.pulumi.cloudinit.outputs.GetConfigResult;
import com.pulumi.core.Output;
import com.pulumi.core.TypeShape;
import com.pulumi.deployment.Deployment;
import com.pulumi.deployment.InvokeOptions;
import com.pulumi.deployment.InvokeOutputOptions;
import java.util.concurrent.CompletableFuture;

public final class CloudinitFunctions {
    /**
     * Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
     * 
     * Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
     * 
     * This is not a generalized utility for producing multi-part MIME messages. It&#39;s feature set is specialized for cloud-init multi-part MIME messages.
     * 
     * ## Example Usage
     * 
     * ### Config
     * 
     * ### hello-script.sh
     * 
     * ### cloud-config.yaml
     * 
     * &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
     * 
     */
    public static Output<GetConfigResult> getConfig() {
        return getConfig(GetConfigArgs.Empty, InvokeOptions.Empty);
    }
    /**
     * Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
     * 
     * Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
     * 
     * This is not a generalized utility for producing multi-part MIME messages. It&#39;s feature set is specialized for cloud-init multi-part MIME messages.
     * 
     * ## Example Usage
     * 
     * ### Config
     * 
     * ### hello-script.sh
     * 
     * ### cloud-config.yaml
     * 
     * &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
     * 
     */
    public static CompletableFuture<GetConfigResult> getConfigPlain() {
        return getConfigPlain(GetConfigPlainArgs.Empty, InvokeOptions.Empty);
    }
    /**
     * Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
     * 
     * Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
     * 
     * This is not a generalized utility for producing multi-part MIME messages. It&#39;s feature set is specialized for cloud-init multi-part MIME messages.
     * 
     * ## Example Usage
     * 
     * ### Config
     * 
     * ### hello-script.sh
     * 
     * ### cloud-config.yaml
     * 
     * &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
     * 
     */
    public static Output<GetConfigResult> getConfig(GetConfigArgs args) {
        return getConfig(args, InvokeOptions.Empty);
    }
    /**
     * Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
     * 
     * Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
     * 
     * This is not a generalized utility for producing multi-part MIME messages. It&#39;s feature set is specialized for cloud-init multi-part MIME messages.
     * 
     * ## Example Usage
     * 
     * ### Config
     * 
     * ### hello-script.sh
     * 
     * ### cloud-config.yaml
     * 
     * &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
     * 
     */
    public static CompletableFuture<GetConfigResult> getConfigPlain(GetConfigPlainArgs args) {
        return getConfigPlain(args, InvokeOptions.Empty);
    }
    /**
     * Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
     * 
     * Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
     * 
     * This is not a generalized utility for producing multi-part MIME messages. It&#39;s feature set is specialized for cloud-init multi-part MIME messages.
     * 
     * ## Example Usage
     * 
     * ### Config
     * 
     * ### hello-script.sh
     * 
     * ### cloud-config.yaml
     * 
     * &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
     * 
     */
    public static Output<GetConfigResult> getConfig(GetConfigArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("cloudinit:index/getConfig:getConfig", TypeShape.of(GetConfigResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
     * 
     * Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
     * 
     * This is not a generalized utility for producing multi-part MIME messages. It&#39;s feature set is specialized for cloud-init multi-part MIME messages.
     * 
     * ## Example Usage
     * 
     * ### Config
     * 
     * ### hello-script.sh
     * 
     * ### cloud-config.yaml
     * 
     * &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
     * 
     */
    public static Output<GetConfigResult> getConfig(GetConfigArgs args, InvokeOutputOptions options) {
        return Deployment.getInstance().invoke("cloudinit:index/getConfig:getConfig", TypeShape.of(GetConfigResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
     * 
     * Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
     * 
     * This is not a generalized utility for producing multi-part MIME messages. It&#39;s feature set is specialized for cloud-init multi-part MIME messages.
     * 
     * ## Example Usage
     * 
     * ### Config
     * 
     * ### hello-script.sh
     * 
     * ### cloud-config.yaml
     * 
     * &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
     * 
     */
    public static CompletableFuture<GetConfigResult> getConfigPlain(GetConfigPlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("cloudinit:index/getConfig:getConfig", TypeShape.of(GetConfigResult.class), args, Utilities.withVersion(options));
    }
}
