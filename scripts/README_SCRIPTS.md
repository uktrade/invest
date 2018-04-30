Clone scripts:

These scripts make it easy to seed development using content from the live
site.

Before using them you need to be able to use  cf ssh  to login to the
app you want to clone.


clone-site.sh     - Clone s3 bucket and database for local developemnt

$ clone-site cf-app db-url


clone-database.sh - Clone database for local development

$ clone-site cf-app db-url


clone-bucket.sh   - Clone s3 bucket for local development

$ clone-site cf-app




Unused scripts:

sass.sh - imported from export, not currently used (as of April 2018)


