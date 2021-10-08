CHANGELOG
=========

## HEAD (Unreleased)
_(none)_

---

## 1.2.1 (2021-10-08)
* Upgrade the version of pulumi/pulumi in the go sdk dependency

## 1.2.0 (2021-10-08)
* Upgrade to v3.9.0 of the pulumi-terraform-bridge. This includes a change to emit input type registrations.

## 1.1.0 (2021-05-27)
* Upgrade to v3.2.1 of the pulumi-terraform-bridge

## 1.0.0 (2021-04-19)
* Depend on Pulumi 3.0, which includes improvements to Python resource arguments and key translation, Go SDK performance,
  Node SDK performance, general availability of Automation API, and more.

## 0.3.0 (2021-04-12)
* Upgrade to pulumi-terraform-bridge v2.23.0

## 0.2.1 (2021-03-23)
* Upgrade to pulumi-terraform-bridge v2.22.1  
  **Please Note:** This includes a bug fix to the refresh operation regarding arrays

## 0.2.0 (2021-03-15)
* Upgrade to pulumi-terraform-bridge v2.21.0
* Release macOS arm64 binary

## 0.1.3 (2021-02-16)
* Upgrade to pulumi-terraform-bridge v2.19.0  
  **Please Note:** This includes a bug fix that stops mutating resources options in the nodejs provider

## 0.1.2 (2021-02-01)
* Upgrade to pulumi-terraform-bridge v2.18.1

## 0.1.1 (2021-01-26)
* Regenerate Go SDK to remove duplicate functionality

## 0.1.0 (2021-01-22)
* Initial creation of the provider against v2.1.0 of the CloudInit Terraform Provider
