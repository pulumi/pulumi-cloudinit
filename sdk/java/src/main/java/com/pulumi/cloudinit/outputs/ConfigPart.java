// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudinit.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class ConfigPart {
    private String content;
    private @Nullable String contentType;
    private @Nullable String filename;
    private @Nullable String mergeType;

    private ConfigPart() {}
    public String content() {
        return this.content;
    }
    public Optional<String> contentType() {
        return Optional.ofNullable(this.contentType);
    }
    public Optional<String> filename() {
        return Optional.ofNullable(this.filename);
    }
    public Optional<String> mergeType() {
        return Optional.ofNullable(this.mergeType);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ConfigPart defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String content;
        private @Nullable String contentType;
        private @Nullable String filename;
        private @Nullable String mergeType;
        public Builder() {}
        public Builder(ConfigPart defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.content = defaults.content;
    	      this.contentType = defaults.contentType;
    	      this.filename = defaults.filename;
    	      this.mergeType = defaults.mergeType;
        }

        @CustomType.Setter
        public Builder content(String content) {
            this.content = Objects.requireNonNull(content);
            return this;
        }
        @CustomType.Setter
        public Builder contentType(@Nullable String contentType) {
            this.contentType = contentType;
            return this;
        }
        @CustomType.Setter
        public Builder filename(@Nullable String filename) {
            this.filename = filename;
            return this;
        }
        @CustomType.Setter
        public Builder mergeType(@Nullable String mergeType) {
            this.mergeType = mergeType;
            return this;
        }
        public ConfigPart build() {
            final var _resultValue = new ConfigPart();
            _resultValue.content = content;
            _resultValue.contentType = contentType;
            _resultValue.filename = filename;
            _resultValue.mergeType = mergeType;
            return _resultValue;
        }
    }
}
