def generate_mermaid_k8s_diagram():
    diagram = """
    graph TD
        A[Kubernetes Cluster] --> B[Namespace]
        B --> C[Pod]
        C --> D[Container]
        C --> E[Service]
        C --> F[ConfigMap]
        C --> G[Secret]
        C --> H[PersistentVolumeClaim]
        C --> I[Ingress]
    """
    return diagram

def generate_description():
    description = """
    This Mermaid diagram represents a Kubernetes cluster with the following components:
    - A: Kubernetes Cluster
    - B: Namespace
    - C: Pod
    - D: Container
    - E: Service
    - F: ConfigMap
    - G: Secret
    - H: PersistentVolumeClaim
    - I: Ingress
    """
    return description

if __name__ == "__main__":
    mermaid_diagram = generate_mermaid_k8s_diagram()
    description = generate_description()

    with open("k8s_diagram.mmd", "w") as file:
        file.write(mermaid_diagram)

    with open("k8s_diagram_description.txt", "w") as file:
        file.write(description)

    print("✨📊 Mermaid diagram for Kubernetes objects has been generated and saved to k8s_diagram.mmd 📂✨")
    print("📄 Description of the Mermaid diagram has been generated and saved to k8s_diagram_description.txt 📂✨")