import json

def main():
    fp = open('/Users/hansrajdas/Downloads/pattern50.csv')
    for line in fp.readlines()[1:]:
        try:
            print(json.loads(('[' + line[2:-3] + ']').replace("'", '"'), strict=False))
        except ValueError:
            print('Conversion to list failed for: %s' % line)

main()
