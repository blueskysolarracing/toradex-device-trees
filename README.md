# Introduction

This repository contains device trees, device tree overlays and related header
files for TorizonCore tools to use. The repository is automatically kept in
sync with the Toradex Linux kernel git tree and the device tree overlay git
tree.

For more details how to use them refer to the [Developer Website
Article](https://developer.toradex.com/knowledge-base/device-tree-overlays).


# toradex-device-trees

The bssr dts to load is dts-arm64/bssr.dts

## How to push the device tree
```bash
torizoncore-builder dt apply device-trees/dts-arm64/bssr.dts
torizoncore-builder union custom-branch
torizoncore-builder deploy custom-branch --remote-host 10.0.1.53 --remote-username torizon --remote-password bssr --reboot
```
