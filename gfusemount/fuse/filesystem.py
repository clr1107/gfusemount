import abc


class FileSystem:
    def __init__(self, name, script_identifier, flags):
        self.name = name
        self.script_identifier = script_identifier
        self.flags = flags

    @abc.abstractmethod
    def popen_args(self, mount):
        return


class SSHFileSystem(FileSystem):
    def __init__(self, flags=None):
        if flags is None:
            flags = dict()

        super().__init__("sshfs", "sshfs", flags)

    def _flags_as_str(self):
        x = []
        for k, v in self.flags.items():
            if v is not None:
                x.append('{}={}'.format(k, v))
            else:
                x.append(k)

        return ','.join(x)

    def popen_args(self, mount):
        args = [self.script_identifier, mount.remote, mount.local]

        self.flags = {**self.flags, **mount.fs_flags}
        if len(self.flags):
            args.append('-o')
            args.append(self._flags_as_str())

        return args
