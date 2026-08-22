#!/usr/bin/env bash
# Copyright (c) Joseph Hale, 2026
# SPDX-License-Identifier: MPL-2.0

set -euo pipefail

if ! command -v mise &>/dev/null; then
	echo "Installing mise..."
	curl https://mise.run | sh
fi

mise trust
mise install
