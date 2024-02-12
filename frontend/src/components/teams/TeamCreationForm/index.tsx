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
import { useForm } from '@mantine/form'
import usePlayers from '@/hooks/usePlayers'

type TeamCreationData = {
  name: string
  firstPlayer?: string
  secondPlayer?: string
}

export default function TeamCreationForm() {
  const { isLoading, data } = usePlayers()
  /**
   * Validation function for first player
   */
  const validateFirstPlayer = (value: string, values: TeamCreationData) => {
    // if first player value is not set
    if (value === undefined) {
      return 'First player is required'
    }
    // if selected same first and second player
    if (values.secondPlayer && value === values.secondPlayer) {
      return 'First and second player cannot be the same'
    }
    return null
  }

  const validateSecondPlayer = (value: string, values: TeamCreationData) => {
    // if selected same first and second player
    if (values.firstPlayer && value === values.firstPlayer) {
      return 'First and second player cannot be the same'
    }
    return null
  }

  const form = useForm({
    initialValues: {
      name: '',
      firstPlayer: undefined,
      secondPlayer: undefined,
    },
    validate: {
      name: (value) => value.trim().length < 2,
      firstPlayer: validateFirstPlayer,
      secondPlayer: validateSecondPlayer,
    },
  })

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
      <form onSubmit={form.onSubmit((values) => console.log(values))}>
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
            {...form.getInputProps('name')}
          />
          <Select
            label="First Player"
            name="firstPlayer"
            placeholder="Pick a player"
            data={playerData}
            {...form.getInputProps('firstPlayer')}
          />
          <Select
            label="Second Player"
            name="secondPlayer"
            placeholder="Pick a player"
            data={playerData}
            {...form.getInputProps('secondPlayer')}
          />
        </Stack>

        <Group justify="center" mt="xl">
          <Button type="submit" size="md">
            Create Team
          </Button>
        </Group>
      </form>
    )
  }

  return <div>Players could not be loaded</div>
}
