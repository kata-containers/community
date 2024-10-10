#!/bin/bash
#
# Copyright (c) 2024 IBM Corporation
#
# SPDX-License-Identifier: Apache-2.0

set -e

export kata_repo="${kata_repo:-github.com/kata-containers/kata-containers}"
export kata_repo_dir="$GOPATH/src/$kata_repo"
export kata_default_branch="${kata_default_branch:-main}"


clone_kata_repo() {
	if [ ! -d "${kata_repo_dir}" ]; then
		mkdir -p "${kata_repo_dir}"
		git clone "https://${kata_repo}.git" "${kata_repo_dir}"
		pushd "${kata_repo_dir}" || exit
		# Checkout to default branch
		git checkout "${kata_default_branch}"
		popd || exit
	fi
}

run_static_checks()
{
	clone_kata_repo
	INSTALL_IN_GOPATH=false bash "${kata_repo_dir}/ci/install_yq.sh"
	bash "${kata_repo_dir}/tests/install_go.sh" -f -p
	bash "${kata_repo_dir}/tests/static-checks.sh" "github.com/kata-containers/community"
}

run_static_checks
