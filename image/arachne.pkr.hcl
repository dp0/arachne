# Use the plugin at https://github.com/dp0/packer-plugin-arm-image to allow us
# to construct ARM images.
packer {
  required_plugins {
    arm-image = {
      version = ">= 0.2.5"
      source  = "github.com/dp0/arm-image"
    }
  }
}

# Download Raspios Full 2023-05-03 and ensure there is enough extra space to
# fit the large model.
source "arm-image" "arachne" {
  iso_checksum = "sha256:73929713e3363e7f8fa1a2cc13999aeed853c667e8539e76244b9cca4cf549cb"
  iso_url      = "https://downloads.raspberrypi.org/raspios_full_arm64/images/raspios_full_arm64-2023-05-03/2023-05-03-raspios-bullseye-arm64-full.img.xz"
  output_filename = "arachne.img"
  last_partition_extra_size = 4*1024*1024*1024
}

build {
  name = "arachne"

  sources = ["source.arm-image.arachne"]

  provisioner "shell" {
    inline = [

      # We will use /opt/arachne for the application and all supporting files
      "mkdir -p /opt/arachne",

      # Install some helpful tools for any debugging/development
      "apt-get update",
      "apt-get -y install vim tmux",
    ]
  }

  # Copy the model
  provisioner "file" {
    source = "../model"
    destination = "/opt/arachne/"
  }

  # Copy the X11 config to prevent display power saving
  provisioner "shell" {
    inline = ["mkdir -p /etc/X11/Xsession.d/"]
  }
  provisioner "file" {
    source = "../etc/98x11-disable-dpms"
    destination = "/etc/X11/Xsession.d/"
  }
  provisioner "shell" {
    inline = ["chmod 0644 /etc/X11/Xsession.d/98x11-disable-dpms"]
  }

}
