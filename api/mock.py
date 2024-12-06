import os

import fastapi as fast

MOCK_DATA = {
  "multiple_choice": [
    {
      "question": "Which type of processor will be faster for tasks with less data that needs to be evaluated quickly?",
      "answer": 1,
      "variants": [
        "GPU",
        "CPU",
        "Neither, the task size doesn't affect performance",
        "Both are equally fast"
      ]
    },
    {
      "question": "Which of the following is true about GPUs and CPUs according to the video transcript?",
      "answer": 3,
      "variants": [
        "A GPU has fewer cores than a CPU, making it less powerful for processing calculations.",
        "The number of cores directly determines the power of a CPU and GPU in terms of their ability to process data.",
        "GPUs are like cargo ships that can handle large amounts of data but at a slower rate compared to CPUs which are more akin to jumbo jets with smaller capacities but higher-speed data processing ability.",
        "CPUs have significantly more cores than GPUs, making them the primary choice for handling graphics and calculations."
      ]
    },
    {
      "question": "What manages the graphics processing clusters and streaming multiprocessors inside the GA102 GPU?",
      "answer": 0,
      "variants": [
        "The engine which manages all the graphics processing clusters and streaming multiprocessors inside.",
        "Display ports for the displays to be plugged into",
        "PCIe pins that plug into the motherboard",
        "Voltage regulator module"
      ]
    },
    {
      "question": "What algorithm generates the lottery ticket number in the context of bitcoin mining described in the video transcript?",
      "answer": 3,
      "variants": [
        "SHA-256",
        "RSA",
        "MD5",
        "Blake2b"
      ]
    },
    {
      "question": "How many Earths filled with people, each performing one calculation per second, would be needed to match the computational power of a single graphics card?",
      "answer": 4400,
      "variants": [
        "44",
        "440",
        "4,400",
        "44,000"
      ]
    }
  ],
  "true_false": [
    {
      "question": "The vertex transformation from model space to world space is the final step in rendering 3D scenes in a GPU.",
      "answer": False
    },
    {
      "question": "Were graphics cards used in the early days of Bitcoin mining because they could perform more SHA-256 hash computations per second compared to modern ASICs?",
      "answer": True
    },
    {
      "question": "Are CPUs more flexible than GPUs in terms of running different types of programs and instructions?",
      "answer": True
    },
    {
      "question": "To convert a vertex from model space into world space, we add the position of the origin of the object in world space to the corresponding X,Y,Z coordinate of the single vertex in model space.",
      "answer": True
    },
    {
      "question": "Do special function units perform more complex operations like division and square root on NVIDIA GPUs?",
      "answer": True
    }
  ]
}

mock_router = fast.APIRouter()

@mock_router.post('/questions')
def generate_questions():
    return MOCK_DATA
