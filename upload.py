import cytomine
import urllib.request

if __name__ == '__main__':

    with cytomine.CytomineJob.from_cli(sys.argv[1:]) as cj:
        filename=None
        if cj.parameters.filename is not None:
            filename=cj.parameters.filename

        url = cj.parameters.url

        response = urllib.request.urlopen(url)
        with f as open(filename,'w'):
            f.write(response.read())

        AttachedFile(
                cj.job,
                domainIdent=cj.job.id,
                filename=filename,
                domainClassName="be.cytomine.processing.Job"
        ).upload()


