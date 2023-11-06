set -x

SRCFILE=${1}
WORKDIR=$(pwd)
TEMPDIR=$( mktemp -d ${WORKDIR}/homebrewery.XXXXXXXX )

function usage() {
    echo
    echo "Usage: $0 <srcfile.md>"
    exit 1
}

function cleanup() {
    rm -rf ${TEMPDIR}
}
trap cleanup EXIT

if [[ -z "${SRCFILE}" ]]; then
    echo
    echo "Need Markdown source file to make into homebrewery"
    usage
fi

# export DOCKER_BUILD=true before running this script to clone and build the container if you need haven't already
if [[ -n "${DOCKER_BUILD}" ]]; then
    pushd ${TEMPDIR}
    git clone git@github.com:naturalcrit/homebrewery.git hb
    cd hb
    git remote add G-Ambatte git@github.com:G-Ambatte/homebrewery.git
    git fetch G-Ambatte
    git checkout remotes/G-Ambatte/experimentalCommandLineBrewProcess
    docker-compose build
fi

docker run -it --rm \
    -v ${WORKDIR}:/usr/src/app/workdir homebrewery \
        node cli/process.js \
        --input /usr/src/app/workdir/${SRCFILE} \
        --output /usr/src/app/workdir/x.html \
        --renderer v3 \
        --overwrite


