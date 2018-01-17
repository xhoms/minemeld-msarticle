# ms-article-miner
Extension to process CSV documents referenced in MS Aticles.

## Configuration
The extension provides you with an example prototype to grab the Microsoft Public IP address space published in the article at the url <https://www.microsoft.com/en-us/download/confirmation.aspx?id=53602>

Use the prototype *MSArticle.msPublicSpace* directly or as a base for your prototypes.

- Mandatory configuration attributes
  - url
- Optional configuration attributes (inherited from CSVFT -> BasePollerFT class)
  - polling_timeout
  - ignore_regex
  - fieldnames
  - delimiter
  - doublequote
  - escapechar
  - quotechar
  - skipinitialspace
  
## Installation

Add it as an external extension as introduced in [MineMeld 0.9.32](https://live.paloaltonetworks.com/t5/MineMeld-Discussions/What-s-new-in-MineMeld-0-9-32/td-p/141261 "What's new in MineMeld 0.9.32")

Use the **git** option with the URL of this repository ( https://github.com/PaloAltoNetworks/minemeld-threatconnect.git )