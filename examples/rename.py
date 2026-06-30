#!/usr/bin/env python3
"""
文件批量重命名工具 (Windows)
用法: python rename.py "C:\\文件夹路径" --suffix "_2024" [--execute]
"""
import argparse
import os
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="批量重命名工具 - 在文件名末尾添加后缀"
    )
    parser.add_argument("folder_path", help="目标文件夹路径")
    parser.add_argument("--suffix", required=True, help="要添加的后缀（不含扩展名）")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="加上此参数才会实际执行重命名，否则仅预览"
    )
    return parser.parse_args()


def validate_args(args):
    if not args.suffix:
        print("错误: 后缀不能为空", file=sys.stderr)
        sys.exit(1)

    folder = Path(args.folder_path)
    if not folder.exists():
        print(f"错误: 路径不存在: {folder}", file=sys.stderr)
        sys.exit(1)
    if not folder.is_dir():
        print(f"错误: 路径不是文件夹: {folder}", file=sys.stderr)
        sys.exit(1)
    return folder


def get_files(folder):
    """获取文件夹内所有文件（排除子文件夹）"""
    return [f for f in folder.iterdir() if f.is_file()]


def preview_changes(files, suffix):
    """预览所有重命名改动"""
    print(f"=== 预览模式 (共 {len(files)} 个文件) ===")
    changes = []
    for i, f in enumerate(files, 1):
        new_name = f.stem + suffix + f.suffix
        new_path = f.parent / new_name
        print(f"[{i}] {f.name} → {new_name}")
        changes.append((f, new_path))
    print("---")
    if not args.execute:
        print("如需执行，请重新运行并加上 --execute")
    return changes


def execute_changes(changes):
    """执行实际重命名"""
    success = 0
    skipped = 0

    for old_path, new_path in changes:
        if new_path.exists():
            print(f"✗ 跳过 (已存在): {old_path.name} (目标文件 {new_path.name} 已存在)")
            skipped += 1
            continue

        try:
            old_path.rename(new_path)
            print(f"✓ 重命名完成: {old_path.name} → {new_path.name}")
            success += 1
        except OSError as e:
            print(f"✗ 重命名失败: {old_path.name} -> {e}")
            skipped += 1

    print(f"---")
    print(f"成功: {success} 个，失败: {skipped} 个")


if __name__ == "__main__":
    args = parse_args()
    folder = validate_args(args)
    files = get_files(folder)

    if not files:
        print("文件夹内没有文件")
        sys.exit(0)

    changes = preview_changes(files, args.suffix)

    if args.execute:
        print("\n=== 执行模式 ===")
        execute_changes(changes)
