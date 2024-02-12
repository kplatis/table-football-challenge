import { Button, Group, Stack, TextInput } from '@mantine/core'
import { useForm } from '@mantine/form'
import { notifications } from '@mantine/notifications'
import axios from 'axios'

type Props = {
  onSuccessFn: () => void
}

export default function PlayerCreationForm({ onSuccessFn }: Props) {
  const form = useForm({
    initialValues: {
      name: '',
    },
    validate: {
      name: (value) => value.trim().length < 2,
    },
  })

  const submit = (values: any) => {
    const data = {
      name: values.name,
    }

    axios.post('http://localhost:8000/players', data).then((response) => {
      if (response.status === 200) {
        notifications.show({
          message: 'Success! Your player has been created.',
        })
        form.reset()
        onSuccessFn()
      }
    })
  }

  return (
    <form onSubmit={form.onSubmit(submit)}>
      <Stack h={300} bg="var(--mantine-color-body)" gap="lg">
        <TextInput
          label="Name"
          placeholder="Player's name"
          name="name"
          variant="filled"
          required={true}
          {...form.getInputProps('name')}
        />
      </Stack>

      <Group justify="center" mt="md">
        <Button type="submit" size="md">
          Create player
        </Button>
      </Group>
    </form>
  )
}
