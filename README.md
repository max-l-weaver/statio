# Statio: Converts tfstate files to HCL compliant tf files

Currently only works with datadog module tfstate files, and only one at a time.

## The Dream
1. Make it less hideous
2. Put some proper error checking in
3. expand it so it can take a tfstate file containing more than one resource
4. Have it create folders too, so your whole infra can be created
5. Link it with terraform wrapper and datadog API for one click conversion
6. Convert tfstate files from other tfstates too.
