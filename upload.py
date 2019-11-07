import cytomine
import urllib.request
import sys
import os
from cytomine.models import AttachedFile

if __name__ == '__main__':
    print(sys.argv[1:])
    base_path = "{}".format(os.getenv("HOME"))

    with cytomine.CytomineJob.from_cli(sys.argv[1:]) as cj:
        filename=None
        if cj.parameters.filename is not None:
            filename=cj.parameters.filename

        url = cj.parameters.url

        response = urllib.request.urlopen(url)
        with open(filename,'wb') as f:
            f.write(response.read())

        AttachedFile(
                cj.job,
                domainIdent=cj.job.id,
                filename=os.path.join(base_path,filename)
                domainClassName="be.cytomine.processing.Job"
        ).upload()


