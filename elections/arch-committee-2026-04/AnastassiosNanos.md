# Anastassios Nanos -> AC

## Summary

Name: Anastassios Nanos, [@ananos](https://github.com/ananos).

Email: ananos@nubificus.co.uk

## Candidacy

### Who I am

I am a Systems Researcher with nearly two decades of experience in systems
software development, specializing in hypervisor technologies, performance
optimization, and secure application execution in multi-tenant Cloud/Edge
environments. My career has been centered around pushing the boundaries of
containerization and virtualization, with a particular focus on making microVM
sandboxes efficient, secure, and broadly applicable.

I've been deeply involved with the Kata Containers project, contributing to
both the Go and Rust runtimes, with particular expertise in Firecracker
integration and hypervisor support. Currently, I balance between academic
research and commercial projects, working on advancing the state-of-the-art in
secure container technologies.

### Why you might know me

- AC member for the past two years
- Contributor to Kata Containers, with involvement in multiple hypervisor
  integration efforts
- Primary focus on Kata<->Firecracker support across both Go and Rust runtimes
- Contributor to CI/infrastructure improvements and hypervisor-related testing
  (k8s on ARM -- still hit & miss)
- Active participant in community calls, gatherings and discussions
- Relatively active public speaker on Kata Containers, representing the project
  at conferences and community events

### Why you might want to elect me

As Kata Containers approaches the critical 4.0 release and the Rust runtime
becomes production-ready, we face significant architectural decisions that will
shape the project's future. I would like to focus on three key areas:

1. Sandboxing Excellence
The effectiveness of Kata as a sandbox depends on how well we integrate with
modern hypervisors and their capabilities. I am committed to ensuring Kata
remains the leading solution for VM-based container isolation by:
- Advocating for hypervisor support with a focus on Firecracker
  as a first-class runtime option
- Ensuring we leverage modern hypervisor features for both performance and
  security
- Maintaining parity between runtimes in terms of sandbox capabilities and
  assurances

2. Runtime-rs Maturity and 4.0 Success
The Rust runtime represents a significant modernization effort for Kata. As we
drive towards 4.0, I want to ensure:
- A smooth transition path for users to adopt the Rust runtime
- Continued investment in Firecracker support as a critical execution path
- Robust feature parity and performance characteristics between Go and Rust
  implementations
- Focus on code quality and testability of the new runtime

3. ARM and CI Infrastructure
With ARM becoming increasingly important in cloud and edge deployments, we must
ensure Kata is a first-class citizen on these platforms. I commit to:
- Advancing ARM CI coverage to match x86 standards
- Supporting diverse ARM use cases, from NVIDIA platforms to other ARM edge
  boards & servers 
- Ensuring CI infrastructure reliability and developer experience across all
  supported architectures
- Working with the community to identify and resolve architecture-specific
  issues

### Additional Perspective

Over the past two years, I've witnessed the Kata community's growth and
maturation. The project is now at an inflection point, we have strong
fundamentals, but the decisions we make around runtimes, hypervisors, and
platforms will determine whether Kata remains the de-facto standard for
VM-based container isolation, or becomes (eventually) a niche solution.

I believe in fostering open collaboration, valuing diverse perspectives, and
maintaining the inclusive environment this community has built. If re-elected,
I will work to bridge technical and community concerns, ensuring that Kata's
architecture evolves to meet both current needs and future challenges.

### Why you might want to elect someone else

My focus is heavily weighted toward runtime and hypervisor integration on ARM
and the Firecracker path, which means other important areas, like container
image handling observability, or CoCo, may not receive equal attention from me.
If the community values a more generalist perspective on the AC, you might
prefer someone with broader interests across Kata's full stack.

Additionally, my time is split between academic research and commercial
projects, which can affect consistency and availability. While I'm committed to
AC responsibilities, someone with undivided focus on Kata might be a better fit
during critical phases like the 4.0 release.

Thanks for considering my candidacy! 

cheers,
Tassos
