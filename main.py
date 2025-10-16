def check_gpu():
    import torch

    if torch.cuda.is_available():
        print("GPU is available!")
        print(f"Number of GPUs: {torch.cuda.device_count()}")
        print(f"Current GPU name: {torch.cuda.get_device_name(0)}")
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        print("Apple's MPS is available!")
        device = torch.device("mps")
    else:
        print("GPU is NOT available. Using CPU.")
        device = torch.device("cpu")

    # Verify the device being used for a tensor
    x = torch.randn(2, 3).to(device)
    print(f"Tensor device: {x.device}")


def main():
    print("Hello from uv-box!\n\n")
    check_gpu()


if __name__ == "__main__":
    main()
