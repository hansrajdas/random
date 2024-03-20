## Using kctrl
### Create package
```sh
kctrl package init

test.sc.tanzu.vmware.com
4
https://github.com/hansrajdas/random
origin/master
source-controller-package/1.1.2/bundle/config/**
```

### Push package to registry and create package repo locally
```sh
kctrl package release --repo-output repo --version 0.1.0

> Enter the registry URL (): hansrajdas/sample-repo
```

### Push package repository to registry
```sh
kctrl package repository release --version 0.1.0-repo.0 --chdir repo/

> Enter the package repository name (sample-repo.carvel.dev): repo0.tanzu.vmware.com
> Enter the registry url (): hansrajdas/sample-repo
```

### Add repository
```sh
kctrl package repository add -r repo-0 --url hansrajdas/sample-repo:0.1.0-repo0 -n hans
```

### Install package install
```sh
kctrl package install -i sc-1 -p test.sc.tanzu.vmware.com --version 0.0.1 -n hans
```

### Delete package install
```sh
kctrl package installed delete -i sc-1 -n hans
```

## Using lever
- Below workload is used for `source-controller-package/1.1.2`
```yaml
apiVersion: carto.run/v1alpha1
kind: Workload
metadata:
  labels:
    lever.tanzu.vmware.com/package-type: carvel
    lever.tanzu.vmware.com/integration-test-runner: "concourse"
    app.kubernetes.io/part-of: gsc
  name: hans-fluxcd-source-controller-package         #! unique name within your namespace
  namespace: ws-tmc-build-integrations                     #! namespace provisioned for your group
spec:
  params:
  - name: destination
    value: harbor-repo.vmware.com/lever/test/hans-fluxcd-source-controller-package
  - name: shepherd_pipeline_id
    value: hans-fluxcd-source-controller-package
  - name: source_pool
    value: gke-127-tap-18-cartov2
  - name: skip-integration-test                         #! skip integration tests for quick verification
    value: true
  source:
    git:
      ref:
        branch: master                                                 #! branch to track
      url: https://github.com/hansrajdas/random.git   #! git repo (https only)
    subPath: source-controller-package/1.1.2
```
