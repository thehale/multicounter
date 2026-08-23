#!/usr/bin/env bash
# Copyright (c) Joseph Hale, 2026
# SPDX-License-Identifier: MPL-2.0

set -euo pipefail

function main() {
	if (bin/ci.sh); then
		echo -e "\n $(green "Tests passed, publishing...")"
		publish
	else
		echo -e "\n $(red "Tests failed, aborting publish.")"
		exit 1
	fi
}

function publish() {
	rm -rf dist
	hatch build

	echo -e "\nEnter your PyPI token:"
	read -r -s token

	hatch publish \
		--user "__token__" \
		--auth "$token"
}

function green() {
	echo -e "\033[0;32m$1\033[0m"
}

function red() {
	echo -e "\033[0;31m$1\033[0m"
}

main
