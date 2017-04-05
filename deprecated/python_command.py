#!/usr/bin/env python
import optparse
import subprocess
import re

def reg_test():
	bt = 'bat|bet|bit'
	m = re.match(bt, 'bat')
	if m is not None: print '1' , m.group()

	m = re.match(bt, 'He bit me!')
	if m is not None: print '2', m.group()

	m = re.search(bt, 'He bit me!')
	if m is not None: print '3', m.group()


def main():
	p = optparse.OptionParser()
	p.add_option('--persion', '-p', default="world")
	p.add_option('--gowhere', '-g', default="go home")
	options, arguments = p.parse_args()
	print options
	if options.persion:
		print '''Hello %s''' % options.persion
	elif options.gowhere:
		print '''Let's %s''' % options.gowhere
	# print '''Hello %s, let's %s''' % (options.persion,  options.gowhere)

if __name__ == '__main__':
	main()
	reg_test()


