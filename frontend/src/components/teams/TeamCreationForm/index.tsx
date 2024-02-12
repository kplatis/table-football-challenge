'use client'

import {
  Button,
  Group,
  Loader,
  Select,
  Stack,
  TextInput,
  Title,
} from '@mantine/core'
import { notifications } from '@mantine/notifications'
import { useForm } from '@mantine/form'
import usePlayers from '@/hooks/usePlayers'
import { validateFirstPlayer, validateSecondPlayer } from './validation'
import axios from 'axios'
import { TeamCreate } from '@/types/teams'

export default function TeamCreationForm() {
  const { isLoading, data } = usePlayers()

  const form = useForm({
    initialValues: {
      name: '',
      firstPlayer: null,
      secondPlayer: null,
    },
    validate: {
      name: (value) => value.trim().length < 2,
      firstPlayer: validateFirstPlayer,
      secondPlayer: validateSecondPlayer,
    },
  })

  const submit = (values: any) => {
    const data: TeamCreate = {
      name: values.name,
      first_player_id: parseInt(values.firstPlayer, 10),
    }
    if (values.secondPlayer !== undefined) {
      data['second_player_id'] = parseInt(values.secondPlayer, 10)
    }

    axios.post('http://localhost:8000/teams', data).then((response) => {
      if (response.status === 200) {
        notifications.show({
          message: 'Success! Your team has been created.',
        })
        form.reset()
      }
    })
  }

  if (isLoading) {
    return (
      <div className="flex justify-center items-center">
        <Loader color="blue" />
      </div>
    )
  }
  if (data) {
    const playerData = data.map((player) => ({
      value: player.id.toString(),
      label: player.name,
    }))

    return (
      <form onSubmit={form.onSubmit(submit)}>
        <Title
          order={2}
          size="h1"
          style={{ fontFamily: 'Greycliff CF, var(--mantine-font-family)' }}
          fw={900}
          ta="center"
        >
          Create a new team
        </Title>
        <Stack h={300} bg="var(--mantine-color-body)" gap="lg">
          <TextInput
            label="Name"
            placeholder="Team's name"
            name="name"
            variant="filled"
            required={true}
            {...form.getInputProps('name')}
          />
          <Group justify="space-between" grow>
            <Select
              label="First Player"
              name="firstPlayer"
              placeholder="Pick a player"
              data={playerData}
              required={true}
              {...form.getInputProps('firstPlayer')}
            />

            <Select
              label="Second Player"
              name="secondPlayer"
              placeholder="Pick a player"
              data={playerData}
              {...form.getInputProps('secondPlayer')}
            />
            <Button>Create new player</Button>
          </Group>
        </Stack>

        <Group justify="center" mt="md">
          <Button type="submit" size="md">
            Create Team
          </Button>
        </Group>
      </form>
    )
  }

  return <div>Players could not be loaded</div>
}
