from mc_bench.util.object_store import Prototype


class KINDS:
    MODEL_RUN = "model_run"
    ARTIFACTS = "artifacts"
    NBT_STRUCTURE_FILE = "nbt-structure-file"
    PROMPT = "prompt"
    SCRIPT = "script"
    RAW_RESPONSE = "raw-response"


runs = Prototype(
    children=[
        Prototype(
            kind=KINDS.MODEL_RUN,
            pattern="model-run/{model_run_id}",
            children=[
                Prototype(
                    kind=KINDS.ARTIFACTS,
                    children=[
                        Prototype(
                            kind=KINDS.NBT_STRUCTURE_FILE,
                            pattern="{name}.nbt",
                        ),
                        Prototype(
                            kind=KINDS.PROMPT,
                            pattern="{name}-prompt.txt",
                        ),
                        Prototype(
                            kind=KINDS.SCRIPT,
                            pattern="{name}-script.py",
                        ),
                    ],
                )
            ],
        )
    ]
)

# runs.get(
#     KINDS.MODEL_RUN,
#     KINDS.ARTIFACTS,
#     KINDS.NBT_STRUCTURE_FILE,
# ).materialize(
#     model_run_id=model_run.id,
#     name=model_run.nbt_file.name,
# )
