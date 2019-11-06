import cytomine
import urllib.request
import sys

if __name__ == '__main__':
    print(sys.argv[1:])

    with cytomine.CytomineJob.from_cli(sys.argv[1:]) as cj:
        filename=None
        if cj.parameters.filename is not None:
            filename=cj.parameters.filename

        url = cj.parameters.url

        response = urllib.request.urlopen(url)
        with open(filename,'w') as f:
            f.write(response.read())

        AttachedFile(
                cj.job,
                domainIdent=cj.job.id,
                filename=filename,
                domainClassName="be.cytomine.processing.Job"
        ).upload()


