import { Center, Loader as MantineLoader } from '@mantine/core'

export default function Loader() {
  return (
    <Center>
      <MantineLoader m="xl" color="blue" data-testid="loader" />
    </Center>
  )
}
