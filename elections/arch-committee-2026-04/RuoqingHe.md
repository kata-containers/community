Name: Ruoqing He

Email: ruoqing.he@lingcage.com

Background:

I'm a senior engineer at LingCage, and my focus is virtualization,
confidential computing and cloud-native on the RISC-V architecture —
more specifically, the software stack related to and including Kata
Containers.

I walked all the way up from rust-vmm to cloud-hypervisor to Kata
Containers, laid down the RISC-V CI infrastructure, and introduced
RISC-V architecture support while actively maintaining it. We have also
been working on Dragonball since last year; that work will be put up for
review in a few months, once we have figured out how to upgrade the
rust-vmm dependencies correctly and elegantly. On the confidential
computing side, I am actively working on RISC-V CoVE, which has made
significant progress recently.

On the RISC-V infrastructure side, we work closely with RISC-V hardware
vendors, testing our code on their FPGAs, QEMU, and prototypes even
before those products are manufactured. RISC-V hardware with the
hypervisor (H) extension is now available, which finally lets us move
the community onto a more reliable CI footing — building, testing, and
running Kata on real RISC-V silicon rather than stopping at the build
step.

In the meantime, I look after the RISC-V runners we already have in the
Kata community, and I will keep our CI — together with the connected and
soon-to-be-connected machines — in good shape, so RISC-V work has solid
ground to progress stably.

In the year ahead, I will be pushing the following forward:

- **Extend and upgrade the runner matrix in Kata self-hosted RISC-V
  runners:** Currently, we are using machines without the hypervisor
  extension solely for building. My goal is to align with other
  architectures and build, test, and run on self-hosted machines.

- **Expand RISC-V support for Kata components:** This is my primary
  focus in the community. I will continue to work out, stabilize, and
  maintain RISC-V architecture support across the project, and make sure
  Kata works properly on RISC-V.

- **Push Kata and CoCo on RISC-V forward:** Drive both Kata and
  Confidential Containers on RISC-V — including the integration of CoVE
  — and keep pace with developments upstream.

Apart from those, I will be committed to helping look after our CI
infrastructure, reviewing and unblocking PRs, and contributing in the
same spirit as the predecessors and current ACs, maintainers, and
contributors in our community.

If given the opportunity to serve on the Architecture Committee, I would
like to make sure RISC-V — as a fast-growing, open architecture — has a
steady voice in Kata's technical direction, and to help the project stay
welcoming to contributors coming in from new hardware ecosystems. Thank
you for considering my nomination.

Cheers,
Ruoqing
