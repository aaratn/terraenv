FROM centos:7

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum update -y && \
    yum install -y python36u python36u-libs python36u-devel python36u-pip git make

ADD https://github.com/tcnksm/ghr/releases/download/v0.13.0/ghr_v0.13.0_linux_amd64.tar.gz .
RUN tar xvzf ghr_v0.13.0_linux_amd64.tar.gz && cd ghr_v0.13.0_linux_amd64 && \
    chmod +x ghr && mv ghr /usr/local/bin
