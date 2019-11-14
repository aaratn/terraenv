class TerraEnv < Formula
  TERRAENV_VERSION = "0.1.0".freeze

  desc "Installs TerraEnv from github"
  homepage "https://vaultproject.io/downloads.html"
  url "https://releases.hashicorp.com/vault/#{TERRAENV_VERSION}/vault_#{TERRAENV_VERSION}_darwin_amd64.zip"
  version TERRAENV_VERSION
  sha256 '0dcc8f5ad55be2a1d485a165f97d7f01a20f95950e32d25a2818ff62328f2f52'

  def install
    bin.install 'TerraEnv'
  end

  test do
   system "#{bin}/terraenv"
  end
end