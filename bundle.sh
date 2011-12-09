#!/bin/bash
# Package theme as .zip file.

GIT_HASH="$(git rev-parse HEAD)"
ZIP_NAME="bootstrap.zip"
HASH_NAME="bootstrap-${GIT_HASH}.zip"

echo "Removing old zip files."
rm ${ZIP_NAME} bootstrap-*.zip
echo

echo "Creating new zip file."
pushd bootstrap
zip -r ../${ZIP_NAME} .
popd
echo

echo "Verifying contents and creating hashed copy."
unzip -l ${ZIP_NAME}
cp ${ZIP_NAME} ${HASH_NAME}
