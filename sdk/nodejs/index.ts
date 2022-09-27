// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { ConfigArgs, ConfigState } from "./config";
export type Config = import("./config").Config;
export const Config: typeof import("./config").Config = null as any;

export { GetConfigArgs, GetConfigResult, GetConfigOutputArgs } from "./getConfig";
export const getConfig: typeof import("./getConfig").getConfig = null as any;
export const getConfigOutput: typeof import("./getConfig").getConfigOutput = null as any;

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;

utilities.lazyLoad(exports, ["Config"], () => require("./config"));
utilities.lazyLoad(exports, ["getConfig","getConfigOutput"], () => require("./getConfig"));
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

// Export sub-modules:
import * as types from "./types";

export {
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "cloudinit:index/config:Config":
                return new Config(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("cloudinit", "index/config", _module)
pulumi.runtime.registerResourcePackage("cloudinit", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:cloudinit") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
