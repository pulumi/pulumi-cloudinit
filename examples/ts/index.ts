import * as cloudinit from "@pulumi/cloudinit";

const resourceConf = new cloudinit.Config("config", {
    gzip: false,
    base64Encode: false,

    parts: [{
        contentType: "text/x-shellscript",
        content: "baz",
        filename: "foobar.sh",
    }]
});

const dsConf = cloudinit.getConfig({
    gzip: false,
    base64Encode: false,

    parts: [{
        contentType: "text/x-shellscript",
        content: "baz",
        filename: "foobar.sh",
    }]
});

export const dsConfig = dsConf.then(x => x.rendered);
export const resourceConfig = resourceConf.rendered;
