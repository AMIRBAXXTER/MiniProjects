
# Compile and run a simple C++ program with asyncio and subprocess
import asyncio


async def compile_cpp(file_path: str, executable_path: str) -> str | None:
    # compiling the C++ code

    compile_process = await asyncio.create_subprocess_exec(
        'g++', file_path, '-o', executable_path,  # compile command
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # waiting for the compilation to finish

    stdout, stderr = await compile_process.communicate()

    if compile_process.returncode != 0:
        print(f"Compilation error: {stderr.decode()}")
        return
    else:
        print("Compilation successful!")
        return f'./{executable_path}'  # executable file path


async def run_executable(executable_path: str) -> None:
    if executable_path is None:
        return

    # run the executable file command

    execute_process = await asyncio.create_subprocess_exec(
        executable_path,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # waiting for the execution to finish

    stdout, stderr = await execute_process.communicate()

    if execute_process.returncode == 0:
        print(f"Output: {stdout.decode()}")
    else:
        print(f"Execution error: {stderr.decode()}")


async def main():
    executable_path = await compile_cpp('example.cpp', 'example2')
    await run_executable(executable_path)


if __name__ == '__main__':
    asyncio.run(main())
