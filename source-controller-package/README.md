### Create package
```sh
kctrl package init

sc.tanzu.vmware.com
4
https://github.com/hansrajdas/random
origin/master
source-controller-package/1.1.2/**/*
source-controller-package/1.1.2/bundle/**/*
source-controller-package/1.1.2/bundle/config/**
```


### Push package to registry and create package repo locally
```sh
# kctrl package release --repo-output repo --version 0.0.1
kctrl package release --repo-output packages --version 0.0.1

> Enter the registry URL (): hansrajdas/sample-repo
```

### Push package repository to registry
```sh
# kctrl package repository release --version 0.0.1-repo.1 --chdir repo/
kctrl package repository release --version 0.0.1-repo.1

> Enter the package repository name (sample-repo.carvel.dev): repo-1.tanzu.vmware.com
> Enter the registry url (): hansrajdas/sample-repo
```

### Add repository
```sh
kctrl package repository add -r repo-1 --url hansrajdas/sample-repo:0.0.1-repo.1 -n hans
```

### Install package install
```sh
kctrl package install -i sc-1 -p sc.tanzu.vmware.com --version 0.0.1 -n hans
```

### Delete package install
```sh
kctrl package installed delete -i sc-1 -n hans
```
