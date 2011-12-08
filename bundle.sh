#!/bin/bash
# Package theme as .zip file.

GIT_HASH="$(git rev-parse HEAD)"
ZIP_NAME="bootstrap-${GIT_HASH}.zip"

echo "Removing old zip files."
if test -n "$(shopt -s nullglob; echo bootstrap-*.zip)"; then
	rm bootstrap-*.zip
fi
echo

echo "Creating new zip file."
pushd bootstrap
zip -r ../${ZIP_NAME} .
popd
echo

echo "Verifying contents."
unzip -l ${ZIP_NAME}
