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

if __name__ == "__main__":
    mermaid_diagram = generate_mermaid_k8s_diagram()
    with open("k8s_diagram.mmd", "w") as file:
        file.write(mermaid_diagram)
    print("Mermaid diagram for Kubernetes objects has been generated and saved to k8s_diagram.mmd")