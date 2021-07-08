provider "azurerm" {
    features {
        
    }
  
}

resource "azurerm_resource_group" "pwcrg" {
    name = "${var.name}"
    location = "${var.location1}"
  
}

