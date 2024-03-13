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
